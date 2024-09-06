@echo off

echo Creating Python environment...
call "C:\Users\%USERNAME%\miniconda3\Scripts\conda" create -n openvino_env python=3.10 -y

echo Activating environment...
call "C:\Users\%USERNAME%\miniconda3\Scripts\activate.bat" openvino_env

echo Installing requirements...
python -m pip install --upgrade pip
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install --pre -U openvino --extra-index-url https://storage.openvinotoolkit.org/simple/wheels/nightly
pip install --pre -U openvino-genai --extra-index-url https://storage.openvinotoolkit.org/simple/wheels/nightly

echo Checking installed packages...
conda list


echo Installation complete!
pause
