# ZConnect API specs

This repo contains the ZConnect API documentation in `openapi.yaml`, which can be used as a template for specific projects.

In order to allow updating of endpoints and core models and paths from ZConnect, there are comment lines encasing definitions from core, such as `### ZC2 builtin paths`. These should be treated as fences and no endpoints should be directly edited.

A script will be created to allow updating of files which rely on the core ZConnect definition.