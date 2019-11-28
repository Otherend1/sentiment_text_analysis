settings = {
    "cache_dir": "~/extra_data/cache_dir",
    "demos": {
        "sentiment_text_analysis": {
            "back": { 
                "port": 8188,
                "ip": 'localhost',
              },
            "front": { 
                "update_database": {
                    "port": 8988,
                    "ip": '0.0.0.0',
                },
                "predict": {
                    "port": 8989,
                    "ip": '0.0.0.0',
                },
            },
        }
    } 
}

