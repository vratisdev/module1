{
    'targets': [
        {
            'target_name': 'module1',
            'sources': [
                'Frontend.cpp',
                'SomeStuff.cpp'
            ],
            'include_dirs': [
                "<!(node -e \"require('nan')\")"
            ],
            'defines': [
                '_EXPORTING'
            ]
        }
    ]
}
