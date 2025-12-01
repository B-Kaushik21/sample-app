pipeline{
    agent any
    environment{
        git_branch='main'
        git_url='https://github.com/B-Kaushik21/sample-app.git'
    }
    stages{
        stage('checkout scm'){
            steps{
                echo "checking out code from github repository"
                git branch: "${git_branch}", url: "${git_url}"
            }
        }
        stage('build stage'){
            steps{
                echo "building the app"
                bat "pip install python"
                bat "python app.py"
            }
        }
        stage('test stage'){
            steps{
                echo "testing the app"
                bat "python *.py > output.txt"
            }
        }
        stage('deploy stage'){
            steps{
                echo "deploying the app"
            }
        }
    }

    post{
        always{
            archiveArtifacts artifacts: 'output.txt', fingerprint: true
        }
    }
}
