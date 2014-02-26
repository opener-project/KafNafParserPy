from distutils.core import setup

setup(name='KafNafParser',
      version='1.1',
      description = 'Parser between KAF and NAF',
      author = 'Ruben Izquierdo',
      url = 'https://github.com/cltl/KafNafParserPy',
      author_email = 'r.izquierdobevia@vu.nl',
      packages = ["KafNafParser.feature_extractor"],
      py_modules = ["KafNafParser.header_data", "KafNafParser.text_data", "KafNafParser.term_data", "KafNafParser.entity_data",
        "KafNafParser.features_data", "KafNafParser.opinion_data", "KafNafParser.constituency_data", "KafNafParser.dependency_data",
        "KafNafParser.coreference_data", "KafNafParser.references_data",
        "KafNafParser.external_references_data", "KafNafParser.span_data",
        "KafNafParser.KafNafParserMod","KafNafParser.term_sentiment_data"],
      data_files = [ ('',['kaf_example.xml','naf.dtd','naf_example.xml',
        'test.py','README.md','LICENSE'])]
      )



