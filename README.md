# Python Manager API

This is a Python module to access the API provided by Manager accounting
software.

## WARNING

Use at your own risk! Always test API usage on a test business first!
Not responsible for any data loss or other problems (see license).

## Description

There is no official API documentation, but the API is meant to be self
documenting by browsing `/api` on a Manager server.

This module design is meant to automate much of the work, eliminate the
need to worry about GUID, and perform basic type checking and validation.

## Installation

`pip install manager_api`

## Configuration

To open a business, you need the server URL, username, password, and the
business name. It is recommended to create a separate user with suitable
permissions for the API access.

If using the local (personal) edition, first use the trial copy of the
server edition to create a user, then use http://localhost:55667 as the
server URL.

## Example Usage

Refer to the included `example.py` for example usage. Running the example
will require a business named "Test Business" and updating the URL and
authorization details.
