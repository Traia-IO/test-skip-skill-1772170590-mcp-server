#!/usr/bin/env python3
"""
Test Skip Skill 1772170590 MCP Server - FastMCP with D402 Transport Wrapper

Uses FastMCP from official MCP SDK with D402MCPTransport wrapper for HTTP 402.

Architecture:
- FastMCP for tool decorators and Context objects
- D402MCPTransport wraps the /mcp route for HTTP 402 interception
- Proper HTTP 402 status codes (not JSON-RPC wrapped)

Generated from OpenAPI: None

Environment Variables:
- SERVER_ADDRESS: Payment address (IATP wallet contract)
- MCP_OPERATOR_PRIVATE_KEY: Operator signing key
- D402_TESTING_MODE: Skip facilitator (default: true)
"""

import os
import logging
import sys
from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple, Union
from datetime import datetime

import requests
from retry import retry
from dotenv import load_dotenv
import uvicorn

load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('test-skip-skill-1772170590_mcp')

# FastMCP from official SDK
from mcp.server.fastmcp import FastMCP, Context
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

# D402 payment protocol - using Starlette middleware
from traia_iatp.d402.starlette_middleware import D402PaymentMiddleware
from traia_iatp.d402.mcp_middleware import require_payment_for_tool, get_active_api_key
from traia_iatp.d402.payment_introspection import extract_payment_configs_from_mcp
from traia_iatp.d402.types import TokenAmount, TokenAsset, EIP712Domain

# Configuration
STAGE = os.getenv("STAGE", "MAINNET").upper()
PORT = int(os.getenv("PORT", "8000"))
SERVER_ADDRESS = os.getenv("SERVER_ADDRESS")
if not SERVER_ADDRESS:
    raise ValueError("SERVER_ADDRESS required for payment protocol")

API_KEY = None

logger.info("="*80)
logger.info(f"Test Skip Skill 1772170590 MCP Server (FastMCP + D402 Wrapper)")
logger.info(f"API: https://date.nager.at")
logger.info(f"Payment: {SERVER_ADDRESS}")
logger.info("="*80)

# Create FastMCP server
mcp = FastMCP("Test Skip Skill 1772170590 MCP Server", host="0.0.0.0")

logger.info(f"✅ FastMCP server created")

# ============================================================================
# TOOL IMPLEMENTATIONS
# ============================================================================
# Tool implementations will be added here by endpoint_implementer_crew
# Each tool will use the @mcp.tool() and @require_payment_for_tool() decorators


# D402 Payment Middleware
# The HTTP 402 payment protocol middleware is already configured in the server initialization.
# It's imported from traia_iatp.d402.mcp_middleware and auto-detects configuration from:
# - PAYMENT_ADDRESS or EVM_ADDRESS: Where to receive payments
# - EVM_NETWORK: Blockchain network (default: base-sepolia)
# - DEFAULT_PRICE_USD: Price per request (default: $0.001)
# - TEST_SKIP_SKILL_1772170590_API_KEY: Server's internal API key for payment mode
#
# All payment verification logic is handled by the traia_iatp.d402 module.
# No custom implementation needed!


# API Endpoint Tool Implementations

@mcp.tool()
@require_payment_for_tool(
    price=TokenAmount(
        amount="1000000000000000",  # 0.001 tokens
        asset=TokenAsset(
            address="0x3e17730bb2ca51a8D5deD7E44c003A2e95a4d822",
            decimals=18,
            network="sepolia",
            eip712=EIP712Domain(
                name="IATPWallet",
                version="1"
            )
        )
    ),
    description="Provide a valid `ISO 3166-1 alpha-2` country code "

)
async def retrieves_detailed_information_about_a_specific_country(
    context: Context,
    countryCode: str = "us"
) -> Any:
    """
    Provide a valid `ISO 3166-1 alpha-2` country code to retrieve country metadata. The response includes commonly used and official country names, the assigned region, and if available neighboring countries based on geographical borders.

    Generated from OpenAPI endpoint: GET /api/v3/CountryInfo/{countryCode}

    Args:
        context: MCP context (auto-injected by framework, not user-provided)
        countryCode: The 2-letter ISO 3166-1 country code (e.g., "US", "GB"). (optional, default: "us")

    Returns:
        API response (dict, list, or other JSON type)

    Example Usage:
        await retrieves_detailed_information_about_a_specific_country(countryCode="us")

        Note: 'context' parameter is auto-injected by MCP framework
    """
    # Payment already verified by @require_payment_for_tool decorator
    # No authentication required for this API - api_key not needed

    try:
        url = f"https://date.nager.at/api/v3/CountryInfo/{countryCode}"
        params = {}
        headers = {}
        # No auth required for this API

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    except Exception as e:
        logger.error(f"Error in retrieves_detailed_information_about_a_specific_country: {e}")
        return {"error": str(e), "endpoint": "/api/v3/CountryInfo/{countryCode}"}


@mcp.tool()
@require_payment_for_tool(
    price=TokenAmount(
        amount="1000000000000000",  # 0.001 tokens
        asset=TokenAsset(
            address="0x3e17730bb2ca51a8D5deD7E44c003A2e95a4d822",
            decimals=18,
            network="sepolia",
            eip712=EIP712Domain(
                name="IATPWallet",
                version="1"
            )
        )
    ),
    description="This endpoint returns all countries for which publ"

)
async def retrieve_the_complete_list_of_all_countries_supported_by_the_nagerdate_api(
    context: Context
) -> Any:
    """
    This endpoint returns all countries for which public-holiday data is available. Each entry includes the country's name and ISO code.

    Generated from OpenAPI endpoint: GET /api/v3/AvailableCountries

    Args:
        context: MCP context (auto-injected by framework, not user-provided)


    Returns:
        API response (dict, list, or other JSON type)

    Example Usage:
        await retrieve_the_complete_list_of_all_countries_supported_by_the_nagerdate_api()

        Note: 'context' parameter is auto-injected by MCP framework
    """
    # Payment already verified by @require_payment_for_tool decorator
    # No authentication required for this API - api_key not needed

    try:
        url = f"https://date.nager.at/api/v3/AvailableCountries"
        params = {}
        headers = {}
        # No auth required for this API

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    except Exception as e:
        logger.error(f"Error in retrieve_the_complete_list_of_all_countries_supported_by_the_nagerdate_api: {e}")
        return {"error": str(e), "endpoint": "/api/v3/AvailableCountries"}


@mcp.tool()
@require_payment_for_tool(
    price=TokenAmount(
        amount="1000000000000000",  # 0.001 tokens
        asset=TokenAsset(
            address="0x3e17730bb2ca51a8D5deD7E44c003A2e95a4d822",
            decimals=18,
            network="sepolia",
            eip712=EIP712Domain(
                name="IATPWallet",
                version="1"
            )
        )
    ),
    description="A long weekend is calculated based on public holid"

)
async def retrieve_all_long_weekends_for_a_given_country_and_year(
    context: Context,
    year: int = 2026,
    countryCode: str = "us",
    availableBridgeDays: int = 1,
    subdivisionCode: Optional[str] = None
) -> Any:
    """
    A long weekend is calculated based on public holidays that create an extended break of at least three consecutive days. Optional bridge days-weekdays between a holiday and a weekend-can be included to identify potential extended leave opportunities.

    Generated from OpenAPI endpoint: GET /api/v3/LongWeekend/{year}/{countryCode}

    Args:
        context: MCP context (auto-injected by framework, not user-provided)
        year: The target year for which long-weekend data should be calculated. (optional, default: 2026)
        countryCode: A valid `ISO 3166-1 alpha-2` country code determining the region of interest. (optional, default: "us")
        availableBridgeDays: The maximum number of bridge days to include when determining long-weekend opportunities. (optional, default: 1)
        subdivisionCode: Narrow the calculation to a specific federal state, province, or subdivision (where supported). (optional)

    Returns:
        API response (dict, list, or other JSON type)

    Example Usage:
        await retrieve_all_long_weekends_for_a_given_country_and_year(year=2026, countryCode="us")

        Note: 'context' parameter is auto-injected by MCP framework
    """
    # Payment already verified by @require_payment_for_tool decorator
    # No authentication required for this API - api_key not needed

    try:
        url = f"https://date.nager.at/api/v3/LongWeekend/{year}/{countryCode}"
        params = {
            "availableBridgeDays": availableBridgeDays,
            "subdivisionCode": subdivisionCode
        }
        params = {k: v for k, v in params.items() if v is not None}
        headers = {}
        # No auth required for this API

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    except Exception as e:
        logger.error(f"Error in retrieve_all_long_weekends_for_a_given_country_and_year: {e}")
        return {"error": str(e), "endpoint": "/api/v3/LongWeekend/{year}/{countryCode}"}


@mcp.tool()
@require_payment_for_tool(
    price=TokenAmount(
        amount="1000000000000000",  # 0.001 tokens
        asset=TokenAsset(
            address="0x3e17730bb2ca51a8D5deD7E44c003A2e95a4d822",
            decimals=18,
            network="sepolia",
            eip712=EIP712Domain(
                name="IATPWallet",
                version="1"
            )
        )
    ),
    description="This endpoint returns all officially recognized pu"

)
async def retrieve_the_list_of_all_public_holidays_for_the_specified_year_and_country(
    context: Context,
    year: int = 2026,
    countryCode: str = "us"
) -> Any:
    """
    This endpoint returns all officially recognized public holidays for the given country and year. Each holiday entry includes the local and English holiday names, information about whether the holiday applies nationally or only in specific subdivisions, and the associated holiday type classifications.

    Generated from OpenAPI endpoint: GET /api/v3/PublicHolidays/{year}/{countryCode}

    Args:
        context: MCP context (auto-injected by framework, not user-provided)
        year: The target year for which public holidays should be retrieved. (optional, default: 2026)
        countryCode: A valid `ISO 3166-1 alpha-2` country code. (optional, default: "us")

    Returns:
        API response (dict, list, or other JSON type)

    Example Usage:
        await retrieve_the_list_of_all_public_holidays_for_the_specified_year_and_country(year=2026, countryCode="us")

        Note: 'context' parameter is auto-injected by MCP framework
    """
    # Payment already verified by @require_payment_for_tool decorator
    # No authentication required for this API - api_key not needed

    try:
        url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}"
        params = {}
        headers = {}
        # No auth required for this API

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    except Exception as e:
        logger.error(f"Error in retrieve_the_list_of_all_public_holidays_for_the_specified_year_and_country: {e}")
        return {"error": str(e), "endpoint": "/api/v3/PublicHolidays/{year}/{countryCode}"}


@mcp.tool()
@require_payment_for_tool(
    price=TokenAmount(
        amount="1000000000000000",  # 0.001 tokens
        asset=TokenAsset(
            address="0x3e17730bb2ca51a8D5deD7E44c003A2e95a4d822",
            decimals=18,
            network="sepolia",
            eip712=EIP712Domain(
                name="IATPWallet",
                version="1"
            )
        )
    ),
    description="By default, the calculation is based on the curren"

)
async def determines_whether_today_is_a_public_holiday_in_the_specified_country_optionally_adjusted_by_a_utc_offset(
    context: Context,
    countryCode: str = "us",
    countyCode: Optional[str] = None,
    offset: int = 0
) -> Any:
    """
    By default, the calculation is based on the current UTC date. You may optionally provide a timezone offset to evaluate the holiday status relative to a different local timezone. This endpoint is optimized for simple command-line or automation workflows where only the HTTP status code is required ``` STATUSCODE=$(curl --silent --output /dev/stderr --write-out "%{http_code}" https://date.nager.at/Api/v3/IsTodayPublicHoliday/AT) if [ $STATUSCODE -ne 200 ]; then # handle error fi ```

    Generated from OpenAPI endpoint: GET /api/v3/IsTodayPublicHoliday/{countryCode}

    Args:
        context: MCP context (auto-injected by framework, not user-provided)
        countryCode: A valid `ISO 3166-1 alpha-2` country code. (optional, default: "us")
        countyCode: Optional. The subdivision code (e.g., state, province) to narrow the check. (optional)
        offset: Optional. UTC timezone offset in hours (range: -12 to +12). (optional, default: 0)

    Returns:
        API response (dict, list, or other JSON type)

    Example Usage:
        await determines_whether_today_is_a_public_holiday_in_the_specified_country_optionally_adjusted_by_a_utc_offset(countryCode="us")

        Note: 'context' parameter is auto-injected by MCP framework
    """
    # Payment already verified by @require_payment_for_tool decorator
    # No authentication required for this API - api_key not needed

    try:
        url = f"https://date.nager.at/api/v3/IsTodayPublicHoliday/{countryCode}"
        params = {
            "countyCode": countyCode,
            "offset": offset
        }
        params = {k: v for k, v in params.items() if v is not None}
        headers = {}
        # No auth required for this API

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    except Exception as e:
        logger.error(f"Error in determines_whether_today_is_a_public_holiday_in_the_specified_country_optionally_adjusted_by_a_utc_offset: {e}")
        return {"error": str(e), "endpoint": "/api/v3/IsTodayPublicHoliday/{countryCode}"}


@mcp.tool()
@require_payment_for_tool(
    price=TokenAmount(
        amount="1000000000000000",  # 0.001 tokens
        asset=TokenAsset(
            address="0x3e17730bb2ca51a8D5deD7E44c003A2e95a4d822",
            decimals=18,
            network="sepolia",
            eip712=EIP712Domain(
                name="IATPWallet",
                version="1"
            )
        )
    ),
    description="The list includes only future holidays relative to"

)
async def retrieve_all_upcoming_public_holidays_occurring_within_the_next_365_days_for_a_given_country(
    context: Context,
    countryCode: str = "us"
) -> Any:
    """
    The list includes only future holidays relative to the current date and is useful for forecasting, event planning, and applications that provide forward-looking holiday insights.

    Generated from OpenAPI endpoint: GET /api/v3/NextPublicHolidays/{countryCode}

    Args:
        context: MCP context (auto-injected by framework, not user-provided)
        countryCode: A valid `ISO 3166-1 alpha-2` country code. (optional, default: "us")

    Returns:
        API response (dict, list, or other JSON type)

    Example Usage:
        await retrieve_all_upcoming_public_holidays_occurring_within_the_next_365_days_for_a_given_country(countryCode="us")

        Note: 'context' parameter is auto-injected by MCP framework
    """
    # Payment already verified by @require_payment_for_tool decorator
    # No authentication required for this API - api_key not needed

    try:
        url = f"https://date.nager.at/api/v3/NextPublicHolidays/{countryCode}"
        params = {}
        headers = {}
        # No auth required for this API

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    except Exception as e:
        logger.error(f"Error in retrieve_all_upcoming_public_holidays_occurring_within_the_next_365_days_for_a_given_country: {e}")
        return {"error": str(e), "endpoint": "/api/v3/NextPublicHolidays/{countryCode}"}


@mcp.tool()
@require_payment_for_tool(
    price=TokenAmount(
        amount="1000000000000000",  # 0.001 tokens
        asset=TokenAsset(
            address="0x3e17730bb2ca51a8D5deD7E44c003A2e95a4d822",
            decimals=18,
            network="sepolia",
            eip712=EIP712Domain(
                name="IATPWallet",
                version="1"
            )
        )
    ),
    description="This global endpoint aggregates upcoming holidays "

)
async def retrieve_all_public_holidays_occurring_worldwide_within_the_next_7_days(
    context: Context
) -> Any:
    """
    This global endpoint aggregates upcoming holidays across all supported countries, enabling international systems to detect near-term events.

    Generated from OpenAPI endpoint: GET /api/v3/NextPublicHolidaysWorldwide

    Args:
        context: MCP context (auto-injected by framework, not user-provided)


    Returns:
        API response (dict, list, or other JSON type)

    Example Usage:
        await retrieve_all_public_holidays_occurring_worldwide_within_the_next_7_days()

        Note: 'context' parameter is auto-injected by MCP framework
    """
    # Payment already verified by @require_payment_for_tool decorator
    # No authentication required for this API - api_key not needed

    try:
        url = f"https://date.nager.at/api/v3/NextPublicHolidaysWorldwide"
        params = {}
        headers = {}
        # No auth required for this API

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    except Exception as e:
        logger.error(f"Error in retrieve_all_public_holidays_occurring_worldwide_within_the_next_7_days: {e}")
        return {"error": str(e), "endpoint": "/api/v3/NextPublicHolidaysWorldwide"}


@mcp.tool()
@require_payment_for_tool(
    price=TokenAmount(
        amount="1000000000000000",  # 0.001 tokens
        asset=TokenAsset(
            address="0x3e17730bb2ca51a8D5deD7E44c003A2e95a4d822",
            decimals=18,
            network="sepolia",
            eip712=EIP712Domain(
                name="IATPWallet",
                version="1"
            )
        )
    ),
    description="This endpoint returns detailed version information"

)
async def retrieve_the_current_version_information_of_the_nagerdate_library(
    context: Context
) -> Any:
    """
    This endpoint returns detailed version information about the Nager.Date implementation running on the server, including the exact NuGet package version used by the API.

    Generated from OpenAPI endpoint: GET /api/v3/Version

    Args:
        context: MCP context (auto-injected by framework, not user-provided)


    Returns:
        API response (dict, list, or other JSON type)

    Example Usage:
        await retrieve_the_current_version_information_of_the_nagerdate_library()

        Note: 'context' parameter is auto-injected by MCP framework
    """
    # Payment already verified by @require_payment_for_tool decorator
    # No authentication required for this API - api_key not needed

    try:
        url = f"https://date.nager.at/api/v3/Version"
        params = {}
        headers = {}
        # No auth required for this API

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

        return response.json()

    except Exception as e:
        logger.error(f"Error in retrieve_the_current_version_information_of_the_nagerdate_library: {e}")
        return {"error": str(e), "endpoint": "/api/v3/Version"}


# TODO: Add your API-specific functions here

# ============================================================================
# APPLICATION SETUP WITH STARLETTE MIDDLEWARE
# ============================================================================

def create_app_with_middleware():
    """
    Create Starlette app with d402 payment middleware.
    
    Strategy:
    1. Get FastMCP's Starlette app via streamable_http_app()
    2. Extract payment configs from @require_payment_for_tool decorators
    3. Add Starlette middleware with extracted configs
    4. Single source of truth - no duplication!
    """
    logger.info("🔧 Creating FastMCP app with middleware...")
    
    # Get FastMCP's Starlette app
    app = mcp.streamable_http_app()
    logger.info(f"✅ Got FastMCP Starlette app")
    
    # Extract payment configs from decorators (single source of truth!)
    tool_payment_configs = extract_payment_configs_from_mcp(mcp, SERVER_ADDRESS)
    logger.info(f"📊 Extracted {len(tool_payment_configs)} payment configs from @require_payment_for_tool decorators")
    
    # D402 Configuration
    facilitator_url = os.getenv("FACILITATOR_URL") or os.getenv("D402_FACILITATOR_URL")
    operator_key = os.getenv("MCP_OPERATOR_PRIVATE_KEY")
    network = os.getenv("NETWORK", "sepolia")
    testing_mode = os.getenv("D402_TESTING_MODE", "false").lower() == "true"
    
    # Log D402 configuration with prominent facilitator info
    logger.info("="*60)
    logger.info("D402 Payment Protocol Configuration:")
    logger.info(f"  Server Address: {SERVER_ADDRESS}")
    logger.info(f"  Network: {network}")
    logger.info(f"  Operator Key: {'✅ Set' if operator_key else '❌ Not set'}")
    logger.info(f"  Testing Mode: {'⚠️  ENABLED (bypasses facilitator)' if testing_mode else '✅ DISABLED (uses facilitator)'}")
    logger.info("="*60)
    
    if not facilitator_url and not testing_mode:
        logger.error("❌ FACILITATOR_URL required when testing_mode is disabled!")
        raise ValueError("Set FACILITATOR_URL or enable D402_TESTING_MODE=true")
    
    if facilitator_url:
        logger.info(f"🌐 FACILITATOR: {facilitator_url}")
        if "localhost" in facilitator_url or "127.0.0.1" in facilitator_url or "host.docker.internal" in facilitator_url:
            logger.info(f"   📍 Using LOCAL facilitator for development")
        else:
            logger.info(f"   🌍 Using REMOTE facilitator for production")
    else:
        logger.warning("⚠️  D402 Testing Mode - Facilitator bypassed")
    logger.info("="*60)
    
    # Add CORS middleware first (processes before other middleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allow all origins
        allow_credentials=True,
        allow_methods=["*"],  # Allow all methods
        allow_headers=["*"],  # Allow all headers
        expose_headers=["mcp-session-id"],  # Expose custom headers to browser
    )
    logger.info("✅ Added CORS middleware (allow all origins, expose mcp-session-id)")
    
    # Add D402 payment middleware with extracted configs
    app.add_middleware(
        D402PaymentMiddleware,
        tool_payment_configs=tool_payment_configs,
        server_address=SERVER_ADDRESS,
        requires_auth=False,  # Only checks payment
        internal_api_key=None,  # No API key needed for public APIs
        testing_mode=testing_mode,
        facilitator_url=facilitator_url,
        facilitator_api_key=os.getenv("D402_FACILITATOR_API_KEY"),
        server_name="test-skip-skill-1772170590-mcp-server"  # MCP server ID for tracking
    )
    logger.info("✅ Added D402PaymentMiddleware")
    logger.info("   - Payment-only mode")
    
    # Add health check endpoint (bypasses middleware)
    @app.route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        """Health check endpoint for container orchestration."""
        return JSONResponse(
            content={
                "status": "healthy",
                "service": "test-skip-skill-1772170590-mcp-server",
                "timestamp": datetime.now().isoformat()
            }
        )
    logger.info("✅ Added /health endpoint")
    
    return app

if __name__ == "__main__":
    logger.info("="*80)
    logger.info(f"Starting Test Skip Skill 1772170590 MCP Server")
    logger.info("="*80)
    logger.info("Architecture:")
    logger.info("  1. D402PaymentMiddleware intercepts requests")
    logger.info("     - Checks payment → HTTP 402 if missing")
    logger.info("  2. FastMCP processes valid requests with tool decorators")
    logger.info("="*80)
    
    # Create app with middleware
    app = create_app_with_middleware()
    
    # Run with uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
        log_level=os.getenv("LOG_LEVEL", "info").lower()
    )
