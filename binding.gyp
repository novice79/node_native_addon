{
  "targets": [
    {
      "target_name": "addon",
      'msvs_precompiled_header': 'src/stdafx.h',
      'msvs_precompiled_source': 'src/stdafx.cpp',
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ 
        "./src/stdafx.cpp",
        "./src/addon.cc",
        "./src/common.cpp",
        "./src/worker.cpp",
        "./src/face.cpp",
        "./src/video.cpp",
        "./src/tts.cpp"
        ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "D:/vcpkg/installed/x64-windows-static/include"
      ],
      'defines': [ 
        # '_HAS_EXCEPTIONS=1',
        # 'NAPI_DISABLE_CPP_EXCEPTIONS', 
        'WIN32_LEAN_AND_MEAN' 
      ],
      'msvs_settings': {
        'VCCLCompilerTool': { 
          # 'WarningLevel': '0',
          'ExceptionHandling': 1 
        },
      },
      'conditions': [
        ['OS=="win"', { 'defines': [ '_HAS_EXCEPTIONS=1' ] }]
      ],
      'variables': {
        'lib_dir%': 'D:/vcpkg/installed/x64-windows-static/lib'
      },
      'libraries': [
        '-l<(lib_dir)/boost_system-vc140-mt.lib'
        ,'-l<(lib_dir)/boost_date_time-vc140-mt.lib'
        ,'-l<(lib_dir)/boost_regex-vc140-mt.lib'
        ,'-l<(lib_dir)/boost_atomic-vc140-mt.lib'
        ,'-l<(lib_dir)/boost_chrono-vc140-mt.lib'
        ,'-l<(lib_dir)/boost_log_setup-vc140-mt.lib'
        ,'-l<(lib_dir)/boost_thread-vc140-mt.lib'
        ,'-l<(lib_dir)/boost_filesystem-vc140-mt.lib'
        ,'-l<(lib_dir)/boost_log-vc140-mt.lib'
        ,'-l<(lib_dir)/boost_locale-vc140-mt.lib'

        ,'-l<(lib_dir)/opencv_calib3d.lib'
        ,'-l<(lib_dir)/opencv_core.lib'
        ,'-l<(lib_dir)/opencv_features2d.lib'
        ,'-l<(lib_dir)/opencv_flann.lib'
        ,'-l<(lib_dir)/opencv_highgui.lib'
        ,'-l<(lib_dir)/opencv_imgcodecs.lib'
        ,'-l<(lib_dir)/opencv_imgproc.lib'
        ,'-l<(lib_dir)/opencv_ml.lib'
        ,'-l<(lib_dir)/opencv_objdetect.lib'
        ,'-l<(lib_dir)/opencv_photo.lib'
        ,'-l<(lib_dir)/opencv_stitching.lib'
        ,'-l<(lib_dir)/opencv_video.lib'
        ,'-l<(lib_dir)/opencv_videoio.lib'

        ,'-l<(lib_dir)/webp.lib'
        ,'-l<(lib_dir)/webpdecoder.lib'
        ,'-l<(lib_dir)/webpdemux.lib'
        ,'-l<(lib_dir)/jpeg.lib'
        ,'-l<(lib_dir)/libpng16.lib'
        ,'-l<(lib_dir)/GlU32.lib'
        ,'-l<(lib_dir)/tiff.lib'
        ,'-l<(lib_dir)/tiffxx.lib'
        ,'-l<(lib_dir)/turbojpeg.lib'
        ,'-l<(lib_dir)/zlib.lib'
        ,'-l<(lib_dir)/lzma.lib'
        ,'-l<(lib_dir)/libeay32.lib'
        ,'-l<(lib_dir)/lapack.lib'
        ,'-l<(lib_dir)/libf2c.lib'
        ,'-l<(lib_dir)/OpenGL32.lib'
        ,'-lvfw32.lib'
        ,'-lcomctl32.lib'

        ,'-l<(lib_dir)/dlib19.17.0_release_64bit_msvc1923.lib'
        ,'-l<(lib_dir)/openblas.lib'
        ,'-l<(lib_dir)/fftw3.lib'
        ,'-l<(lib_dir)/fftw3f.lib'
        ,'-l<(lib_dir)/fftw3l.lib'        
      ],
      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {      
              'DisableSpecificWarnings': ['4503', '4819'],
              # 'WarningLevel': '1',
              # 'WarningLevel': 'TurnOffAllWarnings',       
              # enable rtti
              'RuntimeTypeInfo': 'true',
              'ExceptionHandling': 1
              # ,'RuntimeLibrary': 2, # shared release
            }
          }
        }
      }
    }
  ]
}
