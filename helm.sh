cd backend
ls
helmfile destroy
helmfile apply
sleep 5
kubectl get pods -n new