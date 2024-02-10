pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Lev2607/ha-09.02._python_in_jenkins'
            }
        }
        stage('Setup Python') {
            steps {
                sh '''
                wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
                tar xvf Python-3.10.0.tgz
                cd Python-3.10.0
                ./configure --enable-optimizations
                make
                make altinstall
                '''
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3.10 -m venv venv
                . venv/bin/activate
                '''
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
