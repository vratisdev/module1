{
    'targets': [
        {
            'target_name': 'module1',
            'sources': [
                'Frontend.cpp',
                'SomeStuff.cpp'
            ],
            'include_dirs': [
                '../common',
                '<(module_root_dir)/node_modules/nan'
            ],
            'defines': [
                '_EXPORTING'
            ]
        }
    ]
}
