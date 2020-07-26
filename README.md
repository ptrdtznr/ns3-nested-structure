# ns3-nested-structure feature request

NS-3 (until 3.31) does not allow any nested-structure within the include files. Actually all header/source files have to be in the same directory (cmp. ns3/src/wifi/model). 

```bash
/doc
  ns3-nested-structure.rst
/examples
  ns3-nested-structure-example.cc
  wscript
/helper
  ns3-nested-structure-helper.cc
  ns3-nested-structure-helper.h
/model
  /include
    /another_subfolder
      header.h
    /subfolder
      header2.h
    header1.h
  /src
    main.cpp
  ns3-nested-structure.cc
  ns3-nested-structure.h
wscript
```

## Current behaviour:
During the WAF build process all header files from the current module are copied in to the `build/ns3`. 
```bash
build/ns3
  header.h
  header1.h
  header2.h
```

In case of an include from header1.h to /subfolder/header2.h this might be not resolved (undefined reference). For a better structure of projects it would be *really* helpful to support nested structure like this:.

## Request feature
```bash
build/ns3
  /another_subfolder
    header.h
  /subfolder
    header2.h
  header1.h
```

Issue on Gitlab ns3-repo: https://gitlab.com/nsnam/ns-3-dev/-/issues/242
