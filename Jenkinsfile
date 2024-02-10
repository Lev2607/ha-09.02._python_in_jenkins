pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Lev2607/ha-09.02._python_in_jenkins'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python -m unittest discover'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python setup.py install'
            }
        }
    }
}
