allow_k8s_contexts('rancher-desktop')

docker_build('kbreit/transform-2022-flask', '.', dockerfile='Dockerfile')
docker_build('kbreit/transform-2022-nginx', '.', dockerfile='nginx.Dockerfile')
k8s_yaml('manifests/nginx-deployment.yaml')
k8s_yaml('manifests/nginx-service.yaml')
k8s_yaml('manifests/flask-deployment.yaml')
k8s_yaml('manifests/flask-service.yaml')

k8s_resource(workload='flask', new_name='backend', port_forwards='5000:5000')
k8s_resource(workload='nginx', new_name='frontend', port_forwards='8080:80')
