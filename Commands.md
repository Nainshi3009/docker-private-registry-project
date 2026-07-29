# Docker Private Registry Commands

## Check Docker Version

```bash
docker --version
```

---

## Run Docker Registry

```bash
docker run -d -p 5000:5000 --name registry registry:2
```

---

## Pull Ubuntu Image

```bash
docker pull ubuntu
```

---

## Tag Image

```bash
docker tag ubuntu localhost:5000/my-ubuntu
```

---

## Push Image

```bash
docker push localhost:5000/my-ubuntu
```

---

## Pull Image from Registry

```bash
docker pull localhost:5000/my-ubuntu
```

---

# Authentication Setup

## Generate Password File

```bash
docker run --entrypoint htpasswd httpd:2 -Bbn nainshi mypass123 > auth.txt
```

---

## Remove Existing Registry

```bash
docker rm -f registry
```

---

## Run Authenticated Registry

```bash
docker run -d -p 5000:5000 --name registry ^
-v %cd%/auth.txt:/auth/htpasswd ^
-e REGISTRY_AUTH=htpasswd ^
-e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd ^
-e REGISTRY_AUTH_HTPASSWD_REALM="Registry Realm" ^
registry:2
```

---

## Logout

```bash
docker logout localhost:5000
```

---

## Login

```bash
docker login localhost:5000
```

---

## Test Pull

```bash
docker pull localhost:5000/my-ubuntu
```