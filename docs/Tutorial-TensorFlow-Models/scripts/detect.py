import argparse
import glob
import os
import time

import cv2
import numpy as np
import tensorflow as tf

parser = argparse.ArgumentParser(
    description="object detection tester for webcam, images, and video"
)
# parser.add_argument(
#    "-l",
#    "--labels",
#    default="./exported_graphs/labels.txt",
#    help="Set label file, default: './exported_graphs/labels.txt'",
# )
default_model = "./models/ssd_inception_v2_coco_2018_01_28/frozen_inference_graph.pb"
parser.add_argument(
    "-m", "--model", default=default_model, help=f"Set model file, default: {default_model}",
)
parser.add_argument("-c", "--camera", action="store_true", help="Use web camera, default: False")
default_video = ""
parser.add_argument("-v", "--video", default=default_video, help="Give video file, default: ''")
default_image = ""
parser.add_argument("-i", "--image", default=default_image, help="Give image file, default: ''")
parser.add_argument("--crop", action="store_true", help="Crop object, default: 'False'")
parser.add_argument("--distdir", default=".", help="Output directory, default: '.'")
args = parser.parse_args()

detection_graph = tf.Graph()

mode = "bbox"


def load_graph():
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(args.model, "rb") as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name="")
        return detection_graph


def run_inference_for_single_image(tf_sess, image, graph, image_tensor):
    # Run inference
    output_dict = tf_sess.run(tensor_dict, feed_dict={image_tensor: image})

    # all outputs are float32 numpy arrays, so convert types as appropriate
    output_dict["num_detections"] = int(output_dict["num_detections"][0])
    output_dict["detection_classes"] = output_dict["detection_classes"][0].astype(np.int64)
    output_dict["detection_boxes"] = output_dict["detection_boxes"][0]
    output_dict["detection_scores"] = output_dict["detection_scores"][0]
    return output_dict


def predict_frame(frame, image_tensor, tf_sess):
    # img_test = cv2.imread("./test.jpg")
    img_bgr = cv2.resize(frame, (300, 300))
    # convert bgr to rgb
    image_np = img_bgr[:, :, ::-1]
    image_np_expanded = np.expand_dims(image_np, axis=0)
    start = time.time()
    output_dict = run_inference_for_single_image(
        tf_sess, image_np_expanded, detection_graph, image_tensor
    )
    elapsed_time = time.time() - start
    sec_per_frame = f"sec/frame: {round(elapsed_time, 3)}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, sec_per_frame, (3, 30), font, 1, (0, 255, 255), 1, cv2.LINE_AA)
    h, w, c = frame.shape
    if args.crop:
        box = output_dict["detection_boxes"][0] * np.array([h, w, h, w])
        box = box.astype(np.int)
        return frame[box[0] : box[2], box[1] : box[3]]

    for i in range(output_dict["num_detections"]):
        detection_score = output_dict["detection_scores"][i]
        if detection_score < 0.80:
            continue
        box = output_dict["detection_boxes"][i] * np.array([h, w, h, w])
        box = box.astype(np.int)
        cv2.rectangle(frame, (box[1], box[0]), (box[3], box[2]), (0, 0, 255), 3)
        label_name = str(output_dict["detection_classes"][i])
        if label_name == "85":
            cv2.putText(frame, label_name, (10, 450), font, 2, (0, 255, 255), 2, cv2.LINE_AA)
    return frame


def predict_media(image_tensor, tf_sess):
    if os.path.isdir(args.image):
        images = glob.glob(f"{args.image}/*.jpg")
        for img in images:
            frame = cv2.imread(img)
            image_name = os.path.basename(img)
            frame_result = predict_frame(frame, image_tensor, tf_sess)
            cv2.imwrite(f"{args.distdir}/output_{image_name}", frame_result)
            print(f"Saved output_{image_name}")
    elif args.image:
        frame = cv2.imread(args.image)
        image_name = os.path.basename(args.image)
        frame_result = predict_frame(frame, image_tensor, tf_sess)
        cv2.imwrite(f"{args.distdir}/output_{image_name}", frame_result)
        print(f"Saved output_{image_name}")
    #    elif args.video:
    #        cap = cv2.VideoCapture(args.video)
    #        fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    #
    #        while(cap.isOpened()):
    #            ret, frame = cap.read()
    #            if ret==True:
    #                frame = predict_frame(frame, image_tensor, tf_sess)
    #                frame = cv2.flip(frame,0)
    #
    #                # write the flipped frame
    #                out.write(frame)
    #
    #                cv2.imshow('frame',frame)
    #                if cv2.waitKey(1) & 0xFF == ord('q'):
    #                    break
    #            else:
    #                break
    #
    #        # Release everything if job is finished
    #        cap.release()
    #        out.release()
    #        cv2.destroyAllWindows()

    else:
        # VideoCapture を作成する。
        cap = cv2.VideoCapture(0)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        # VideoWriter を作成する。
        fourcc = cv2.VideoWriter_fourcc(*"DIVX")
        writer = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            frame_result = predict_frame(frame, image_tensor, tf_sess)

            # Save result video
            writer.write(frame_result)

            # Display the resulting frame
            cv2.imshow("frame", frame_result)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":

    print("Loading graph...")
    detection_graph = load_graph()
    print("Graph is loaded")

    tf_config = tf.ConfigProto()
    tf_config.gpu_options.allow_growth = True
    with detection_graph.as_default():
        tf_sess = tf.Session(config=tf_config)
        ops = tf.get_default_graph().get_operations()
        all_tensor_names = {output.name for op in ops for output in op.outputs}
        tensor_dict = {}
        for key in [
            "num_detections",
            "detection_boxes",
            "detection_scores",
            "detection_classes",
            "detection_masks",
        ]:
            tensor_name = key + ":0"
            if tensor_name in all_tensor_names:
                tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(tensor_name)

        image_tensor = tf.get_default_graph().get_tensor_by_name("image_tensor:0")

        predict_media(image_tensor, tf_sess)
