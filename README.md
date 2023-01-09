# Loogger for Serial

## Setup and run the application

1. First, make sure you have conda installed on your machine. If you don't, you can download it from the [Anaconda website](https://www.anaconda.com/).

2. Create a new conda environment by running the following command in your terminal:

    ```shell
    conda create -n BASE python=3.11 -c conda-forge
    ```

3. Activate the environment by running:

    ```shell
    conda activate BASE
    ```

4. Clone the project from GitHub/Bitbucket to your local machine.

5. Navigate to the project directory in your terminal and run the following command to install the necessary dependencies:

    ```shell
    pip install -r requirements.txt
    ```

6. Run the application help menu by running the following command in the terminal:

    ```shell
    python logger.py -h
    ```

    Or you can use the following command as an exaample:

    ```shell
    python logger.py -n AVR128DA48 -p COM3 -b 115200
    ```

7. To exit the application, press <kbd>CTRL</kbd> + <kbd>C</kbd> in the terminal. To deactivate the conda environment, type the following command in the terminal:

    ```shell
    conda deactivate
    ```
