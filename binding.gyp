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
                'node_modules/nan/'
            ],
            'defines': [
                '_EXPORTING'
            ]
        }
    ]
}
