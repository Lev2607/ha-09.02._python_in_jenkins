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
                ./configure --enable-optimizations --prefix=$HOME/python3.10
                make
                make altinstall
                '''
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                $HOME/python3.10/bin/python3.10 -m venv --without-pip venv
                . venv/bin/activate
                curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                python get-pip.py
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
