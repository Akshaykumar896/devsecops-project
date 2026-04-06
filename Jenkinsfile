pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build') {
            steps {
                echo 'Running Python app...'
                sh 'python3 app.py'
            }
        }
    }
}
