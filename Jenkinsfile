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
                  // Create a new virtual environment
                  sh "/usr/bin/python3 -m venv ${VIRTUAL_ENV}"
                  
                  // Install dependencies
                  sh "${VIRTUAL_ENV}/bin/pip install -r requirements.txt"
                  
                  // Install coverage and bandit
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
                  // Run tests with pytest
                  sh "${VIRTUAL_ENV}/bin/pytest"
              }
          }
      }

      stage('Coverage') {
          steps {
              script {
                  // Run coverage and generate a report
                  sh "${VIRTUAL_ENV}/bin/coverage run -m pytest"
                  sh "${VIRTUAL_ENV}/bin/coverage report"
                  sh "${VIRTUAL_ENV}/bin/coverage html" // Generates an HTML report
              }
          }
          post {
              always {
                  // Publish the HTML report
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
                  // Run bandit for security scanning
                  sh "${VIRTUAL_ENV}/bin/bandit -r ."
              }
          }
      }

      stage('Deploy') {
          steps {
              script {
                  echo "Deploying application..."
                  // Example deployment command
                  // This can be replaced with an actual deployment script or SSH command
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
