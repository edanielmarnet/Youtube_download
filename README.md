# Youtube_download
 test for music and video downloads from youtube.

In the terminal convert the ui file to py with the command in the directory of the file location:


## pyuic5 'nome do frame'.ui -o 'nome do frame'.py -x


if there are images, convert images from .qrc to .py format


## pyrcc5 'nome da imagem'.qrc -o 'nome da imagem'.py


to create the executable file run the command in the terminal in the file directory location


## pyinstaller --onefile --noconsole 'nome do arquivo que será convertido'.py
