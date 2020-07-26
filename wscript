# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# def options(opt):
#     pass

# def configure(conf):
#     conf.check_nonfatal(header_name='stdint.h', define_name='HAVE_STDINT_H')

def build(bld):
    module = bld.create_ns3_module('ns3-nested-structure', ['core'])
    module.source = [
        'model/ns3-nested-structure.cc',
        'helper/ns3-nested-structure-helper.cc',
        ]

    module_test = bld.create_ns3_module_test_library('ns3-nested-structure')
    module_test.source = [
        'test/ns3-nested-structure-test-suite.cc',
        ]
    # Tests encapsulating example programs should be listed here
    if (bld.env['ENABLE_EXAMPLES']):
        module_test.source.extend([
        #    'test/ns3-nested-structure-examples-test-suite.cc',
             ])

    headers = bld(features='ns3header')
    headers.module = 'ns3-nested-structure'
    headers.source = [
        'model/ns3-nested-structure.h',
        'helper/ns3-nested-structure-helper.h',
        ]

    if bld.env.ENABLE_EXAMPLES:
        bld.recurse('examples')

    # bld.ns3_python_bindings()

