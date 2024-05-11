# Vector Explorer (Now in Flet!)

This is a work in progress. Don't use it yet!

This is a fork of the Vector Explorer app, which was itself a fork of the Cosmo explorer. What a wild ride this little robot has gone on.

To run the app:

```
flet run [app_directory]
```

Currently, the only thing that works is the Chat tab, and it only works under very fiddly circumstances. Working on making this virtualizable so it can be deployed as a web app.

### Requirements: 

* the [updated version of the Wirepod Vector SDK*](https://github.com/kercre123/wirepod-vector-python-sdk) from kercre123. This is required to run the app; running the original SDK doesn't work well.
* a wirepod-enabled Vector robot 
