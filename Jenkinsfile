pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Sagi101/WorldOfGames.git'
            }
        }
        stage('Build Docker') {
            steps {
                bat 'docker build -t sagi101/wog .'
            }
        }
        stage('Run') {
            steps {
               bat 'docker compose up -d'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pip install selenium'
               bat 'python e2e.py'
            }
        }
         stage('Finalize') {
            steps {
                bat 'docker compose down'
                bat 'docker push sagi101/wog'
            }
        }
    }
}
