pipeline {
    agent any

    stages {
        stage('Clean Project') {
            steps {
                echo '--- Cleaning the project ---'
                bat 'kubectl delete -f nodeport.yaml --ignore-not-found=true'
                bat 'pause 10'
                bat 'kubectl delete -f nodeport.yaml --ignore-not-found=true'
                bat 'pause 10'
                bat 'docker image rm -f jango-chat:1.0 2>nul || exit 0'
                bat 'pause 10'
                bat 'docker image rm -f jango-chat:1.0 2>nul || exit 0'
                bat 'pause 10'
                bat 'kubectl delete secret django-superuser-secret'
                bat 'pause 10'
                bat 'npm run clean_windows 2>nul || exit 0'
            }
        }

        stage('Build Project') {
            steps {
                echo '--- Building the project ---'
                bat 'docker build -t jango-chat:1.0 .'
            }
        }

        stage('Create Secret to Kubernetes') {
            steps {
                echo '--- Creating Secret to Kubernetes ---'
                bat 'kubectl create secret generic django-superuser-secret --from-literal=DJANGO_SUPERUSER_USERNAME=angelahack1 --from-literal=DJANGO_SUPERUSER_EMAIL=angelakimichellle@hotmail.com --from-literal=DJANGO_SUPERUSER_PASSWORD=128011LouderDuHastMercie'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '--- Deploying to Kubernetes ---'
                bat 'kubectl apply -f nodeport.yaml'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Project successfully deployed!'
        }
        failure {
            echo 'Pipeline failed. Please check the console output.'
        }
    }
}