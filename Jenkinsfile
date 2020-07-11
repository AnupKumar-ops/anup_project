pipeline {
    agent {
        docker { image 'alpine:latest' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'uname -a'
            }
        }
    }
}
