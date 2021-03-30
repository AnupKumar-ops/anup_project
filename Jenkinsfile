pipeline {
    agent any
    
    triggers {
        pollSCM '* * * * *'
    }
     

    stages {
        stage('SCM Checkout') {
            steps {
                 git 'https://github.com/AnupKumar-ops/anup_project.git'
            }
        }
    }
}
