pipeline {
  agent any

  environment {
      VIRTUAL_ENV = 'myenv'
      PATH = "${env.WORKSPACE}/${VIRTUAL_ENV}/bin:${env.PATH}"
  }

  stages {
      stage('Setup') {
          steps {
              script {
                  if (!fileExists("${env.WORKSPACE}/${VIRTUAL_ENV}")) {
                      sh "python3 -m venv ${VIRTUAL_ENV}"
                  }
                  sh "${VIRTUAL_ENV}/bin/pip install -r requirements.txt"
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

      stage('Deploy') {
          steps {
              script {
                  // Deployment logic, e.g., pushing to a remote server
                  echo "Deploying application..."
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
