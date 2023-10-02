# home_buddy_interview_task

## Run the project
How to build and run the project

Ensure you have Git and Python3 installed
 
Clone the project 
```bash
git clone https://github.com/XeniaBerkut/home_buddy_interview_task.git
```
Go to the directory
```bash
cd home_buddy_interview_task/
```
### Run the project via installing environment and requirements

Create virtual python environment
```bash
virtualenv venv
```
Activate virtual python environment
```bash
source venv/bin/activate
```
Install all the requirements
```bash
pip install -r requirements.txt
```
Export Python path
#### Linux
```bash
export PYTHONPATH=src:$PYTHONPATH

```
#### Windows
```bash
set PYTHONPATH=src:$PYTHONPATH

```
Run tests

```bash
pytest -v