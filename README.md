# CADIHELP 

_Recognize Vietnam Sign Language in real time._

Visit https://cadihelp.heroku.com for more, if you need detail design and deep learning model, please contact to taquangngoc.hh3@gmail.com.

## Agenda
1. [Configuration](#configuration)  
2. [Features](#features)
3. [Reference](#reference)
4. [License](#license)

## Configuration
-   Tech stack: [Django](https://www.djangoproject.com/), [TensorFlow.js](https://www.tensorflow.org/js), [Mediapipe](https://google.github.io/mediapipe/).
-   Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all package.

    ```bash
    pip install virtualenv
    virtualenv <yourFoldername>
    cd <yourFoldername>

    # in Window OS, activate virtualenv
    scripts\activate
    # in Linux OS, activate virtualenv
    source bin/activate
    ```

-   Use the [git](https://git-scm.com/) to install project.

    ```bash
    git clone https://github.com/tangoc2712/blogw-loginsys
    cd blogw-loginsys
    pip install -r requirement.txt
    ```
## Features
- Recognition with real-time video input and corresponding audio, word output

 ![](https://raw.githubusercontent.com/tangoc2712/blogw-loginsys/main/images/main.png)

 - Gameplay to learn Alphabet character VSL

![](https://raw.githubusercontent.com/tangoc2712/blogw-loginsys/main/images/game.png)

- Blogging

![](https://raw.githubusercontent.com/tangoc2712/blogw-loginsys/main/images/blog.jpeg)

## Reference
- [rabBit64](https://github.com/LeeYongchao/Sign-language-recognition-with-RNN-and-Mediapipe)

- [Nicholas Renotte](https://github.com/nicknochnack/ActionDetectionforSignLanguage)
## License

-   [MIT](https://choosealicense.com/licenses/mit/)
