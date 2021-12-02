#!/usr/bin/env python3

# This script simulates the API

import settings

settings.__init__ ()

import endpoints.click_ad
import endpoints.view_ad

import functions.add_cors_headers # Without this you will get an error complaining
                                  # that we are not returning a 'valid response'

settings.app.run(
    host=settings.api_host,
    port=settings.api_port
)
