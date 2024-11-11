pipeline {
  agent any

  environment {
      VIRTUAL_ENV = 'myenv'
      PATH = "${env.WORKSPACE}/${VIRTUAL_ENV}/bin:${env.PATH}"
      PYTHONPATH = "${env.WORKSPACE}"
  }

  stages {
      stage('Setup') {
          steps {
              script {
                  sh "/usr/bin/python3 -m venv ${VIRTUAL_ENV}"
                  sh "${VIRTUAL_ENV}/bin/pip install -r requirements.txt"
                  sh "${VIRTUAL_ENV}/bin/pip install coverage bandit"
              }
          }
      }

      stage('Lint') {
          steps {
              script {
                  sh "${VIRTUAL_ENV}/bin/flake8 app.py"
              }
          }
      }

      stage('Test') {
          steps {
              script {
                  sh "${VIRTUAL_ENV}/bin/pytest"
              }
          }
      }

      stage('Coverage') {
          steps {
              script {
                  sh "${VIRTUAL_ENV}/bin/coverage run -m pytest"
                  sh "${VIRTUAL_ENV}/bin/coverage report"
                  sh "${VIRTUAL_ENV}/bin/coverage html" 
              }
          }
          post {
              always {
                  publishHTML([allowMissing: false, 
                               alwaysLinkToLastBuild: true, 
                               keepAll: true, 
                               reportDir: 'htmlcov', 
                               reportFiles: 'index.html', 
                               reportName: 'Coverage Report'])
              }
          }
      }

        stage('Security Scan') {
            steps {
                script {
                    sh "${VIRTUAL_ENV}/bin/bandit -r . --exclude myenv"
                }
            }
        }

      stage('Deploy') {
          steps {
              script {
                  echo "Deploying application..."
                  sh "echo 'Deploying to remote server or local environment'"
              }
          }
      }
  }

  post {
      always {
          cleanWs()
      }
  }
}
