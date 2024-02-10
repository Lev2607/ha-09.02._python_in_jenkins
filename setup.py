stage('Deploy') {
    steps {
        sh 'python main.py'
    }
}
