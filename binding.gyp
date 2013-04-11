{
  "targets": [
    {
      "target_name": "fuse",
      "sources": [
        "src/node_fuse.cc",
        "src/bindings.cc",
        "src/file_info.cc",
        "src/filesystem.cc",
        "src/reply.cc"
      ],
      "libraries": [
        "<!@(pkg-config fuse --libs)"
      ],
      "include_dirs": [
        "<!@(pkg-config fuse --cflags-only-I | sed s/-I//g)"
      ],
      "defines": [
        "FUSE_USE_VERSION=27",
        "_FILE_OFFSET_BITS=64"
      ]
    }
  ]
}