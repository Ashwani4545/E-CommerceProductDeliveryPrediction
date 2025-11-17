def test_pipeline_smoke():
    import etl.pipeline as pipeline
    assert callable(pipeline.run)
