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
                bat  ' "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" app.py'
            }
        }
    }
}
