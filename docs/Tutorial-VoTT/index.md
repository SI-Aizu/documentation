# VoTT Tutorial

Tutorial for annotation with [VoTT v2.2.0](https://github.com/microsoft/VoTT/releases/tag/v2.2.0)

> [microsoft/VoTT - GitHub](https://github.com/microsoft/VoTT)
>
> Visual Object Tagging Tool: An electron app for building end to end Object Detection Models from Images and Videos.



## Download VoTT

Go to [releases page] and check the latest version.

[releases page]: https://github.com/microsoft/VoTT/releases

### Install to macOS

```sh
export VOTT_VERSION="2.2.0"
wget "https://github.com/microsoft/VoTT/releases/download/v${VOTT_VERSION}/vott-${VOTT_VERSION}-darwin.dmg"
hdiutil mount "vott-${VOTT_VERSION}-darwin.dmg"
cp -r "/Volumes/vott ${VOTT_VERSION}/vott.app" /Applications/
hdiutil detach "/Volumes/vott ${VOTT_VERSION}"
open -a vott.app
```

### Install to Linux

```sh
export VOTT_VERSION="2.2.0"
wget "https://github.com/microsoft/VoTT/releases/download/v${VOTT_VERSION}/vott-${VOTT_VERSION}-linux.snap"
sudo snap install --dangerous "./vott-${VOTT_VERSION}-linux.snap"
```

### Install to Windows

TBW.



## Setup a new project

You can use [vott-tutorial/sample_project] for your tutorial.

[vott-tutorial/sample_project]: https://github.com/SI-Aizu/vott-tutorial/tree/master/sample_project

The following is a project structure. Put your images in a `source` directory.

```
sample_project
├── source
│   ├── car_1.jpg
│   ├── car_2.jpg
│   └── car_3.jpg
└── target
```

1. Open VoTT app
2. Click `New Project`
3. Fill `Display Name`

![project](https://user-images.githubusercontent.com/30958501/85507855-fc3f1e80-b62d-11ea-84af-82b2b424f6d2.jpg)

### Source Connection

1. Click `Add Connection`
2. Fill `Display Name`
3. `Provider`
   1. Select `Local File System`
   2. Select your `source` folder
4. Click `Save Connection`
5. Set the connection to `Source Connection`

![source_connection](https://user-images.githubusercontent.com/30958501/85507859-fcd7b500-b62d-11ea-93d0-b5ed82414bad.jpg)

### Target Connection

1. Click `Add Connection`
2. Fill `Display Name`
3. `Provider`
   1. Select `Local File System`
   2. Select your `target` folder
4. Click `Save Connection`
5. Set the connection to `Target Connection`

Finally, click `Save Project`



## Annotation

You can also view [the video that shows a manner of annotation](https://github.com/SI-Aizu/vott-tutorial/releases/download/v0.1.0/sample.mp4).

### Keyboard Shortcuts

| Shortcut key | Command |
|---|---|
| `W` or `ArrowUp` | Previous Asset |
| `S` or `ArrowDown` | Next Asset |
| `Ctrl + Arrowkey` | Move Region |
| `Ctrl + Alt + Arrowkey` | Shrink Region |
| `Ctrl + Shift + Arrowkey` | Expand Region |

### Mouse Controls

| Mode | Command |
|---|---|
| Two-point mode | Hold down `Ctrl` while creating a region |
| Square mode | Hold down `Shift` while creating a region |
| Multi-select mode | Hold down `Shift` while selecting regions |
| Exclusive Tracking mode | `Ctrl + N` to block frame UI allowing a user to create a region on top of existing regions |

### Tag ordering

Hotkeys of 1 through 0 are assigned to the first ten tags.
These can be reordered by using the up/down arrow icons in in the tag editor pane.

### Tag locking

A tag can be locked for repeated tagging using the lock icon at the top of the tag editor pane.
Tags can also be locked by combining Ctrl or Cmd and the tag hotkey, i.e. `Ctrl + 2` would lock the second tag in the list.

![tags_editor](https://user-images.githubusercontent.com/30958501/85507869-fe08e200-b62d-11ea-9a5e-3da01459eec6.jpg)



## Check your progress

![progress](https://user-images.githubusercontent.com/30958501/85507845-fa755b00-b62d-11ea-96fe-8e50b9263eb1.jpg)



## Export dataset

1. Go to **Export Settings** and set your exporting format.
2. Click `Save Export Settings`.
3. Click `Export button` on the tags editor.

![export_settings](https://user-images.githubusercontent.com/30958501/85507840-f8ab9780-b62d-11ea-8b81-b80df8634890.jpg)
![tags_editor_export](https://user-images.githubusercontent.com/30958501/85507863-fd704b80-b62d-11ea-98b8-b44139164ff0.jpg)

The following is a project structure after exporting.

```
sample_project
├── source
│   ├── car_1.jpg
│   ├── car_2.jpg
│   └── car_3.jpg
└── target
    ├── 32db62ab992c250ba2312fdc3babc444-asset.json
    ├── 41e0a9f85a8d20040692c8390317d3ce-asset.json
    ├── 7ce54d9571515f858d958f3a20cd3ff7-asset.json
    ├── sample_project-TFRecords-export
    │   ├── car_1.tfrecord
    │   ├── car_2.tfrecord
    │   ├── car_3.tfrecord
    │   └── tf_label_map.pbtxt
    └── sample_project.vott
```



## Open existing project

You can use [vott-tutorial/sample_existing_project] as an example for opening local project.

[vott-tutorial/sample_existing_project]: https://github.com/SI-Aizu/vott-tutorial/tree/master/sample_existing_project

1. Click `Open Local Project`
2. Select VoTT project file (e.g. `sample_project.vott`)
