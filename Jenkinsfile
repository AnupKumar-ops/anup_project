def VendorName              = "Cisco"
def Product                 = "War/Jar"
def Version                 = "vnf_v1.1"
def ArtifactoryUrl          = "http://localhost:8082/artifactory"
def ArtifactoryCredentials = "jfrog"

pipeline {
    agent any
    
    triggers {
        pollSCM '* * * * *'
    }
     

    stages {
        stage('SCM Checkout') {
            steps {
                 git 'https://github.com/AnupKumar-ops/vanakkam-world.git'
            }
        }
        stage('mvn build') {
            
            steps {
                tool name: 'maven-3.6.3', type: 'maven'
                withMaven(maven: 'maven-3.6.3') {
                    sh 'mvn clean install'
                }    
            }
        }
        stage('junit test reports') {
            steps {
                junit keepLongStdio: true, testResults: '**/target/surefire-reports/TEST-*.xml'
                //step([$class: 'JUnitResultArchiver', checksName: '', testResults: '**/target/surefire-reports/TEST-*.xml'])
            }
        }
        stage('store to artifactory') {
            steps {
              script {
                 def server = Artifactory.newServer url: "${ArtifactoryUrl}", credentialsId: "${ArtifactoryCredentials}"
                 def uploadSpec = """{
                                      "files": [
                                          {
                                             "pattern": "${WORKSPACE}/**/target/*.war",
                                             "target": "${VendorName}/${Product}/${Version}/"
                                          },
                                          {
                                             "pattern": "${WORKSPACE}/**/target/*.jar",
                                             "target": "${VendorName}/${Product}/${Version}/"
                                          }   
                                       ]
                                  }"""
                server.upload spec: uploadSpec
             }
          }
       }
    }
    post {
                failure {
                    emailext body: "job ${JOB_NAME} with build ${BUILD_NUMBER} failed. Check console output at ${BUILD_URL}", subject: 'fail build', to: 'kumar.abcdef.anup@gmail.com'
                }
    }
}
