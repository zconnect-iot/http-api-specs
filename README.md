# ZConnect API specs

This repo contains the ZConnect API documentation in `openapi.yaml`, which can be used as a template for specific projects.

In order to allow updating of endpoints and core models and paths from ZConnect, there are comment lines encasing definitions from core, such as `### ZC2 builtin paths`. These should be treated as fences and no changes should be made between them.

## Viewing API specs

The easiest way to get viewing/editing is to install "Redoc up", which will allow you to serve a local auto refreshing instance of redoc.

Install:
```
npm install -g redocup
```

Run in your specs repo:

```
redocup -w openapi.yaml
```

visit http://localhost:5000


## Updating API specs

There's an updater script in this repo which will replace the fenced off blocks with those from the base ZConnect 2 specs. This makes it easy to keep the base components up-to-date.

To run, it's easiest to do from the ZC2 specs repo (i.e. here), but you need to know the path to the specs you want to update. To run:

```
python update_base_specs.py --spec ../<path to your specs>/openapi.yaml
```

After this you will just need to commit your project specs. Any changes made to the base in that project will be lost, so do be careful!