Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { dockerfile true }
    stages {
        stage('check') {
            steps {
                sh 'python3 manipulate_string.py'
            }
        }
        stage('test') {
            steps {
                sh 'python3 -m unittest test_manipulate_string.py'
            }
        }
    }
}