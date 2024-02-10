pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Lev2607/ha-09.02._python_in_jenkins'
            }
        }
        stage('Setup Python') {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt-get install -y python3 python3-venv python3-pip'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python -m unittest'
            }
        }
	stage('Deploy') {
            steps {
                sh 'python setup.py install'
            }
        }
    }
}
