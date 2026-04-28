# Exposing all configuration constants as Python variables
import pathlib


# This path
BASE = pathlib.Path(__file__).parent

# Paths to each resolver file
RESOLVER_FILES = {
    "WHITE_DNS_UDP": BASE / "resolvers/white_dns_udp_resolvers.txt",
    "IRAN_CIDRS_RAW": BASE / "resolvers/iran_cidrs_raw.txt",
    "BUILTIN_RESOLVERS": BASE / "resolvers/builtin_resolvers.txt",
}

# --- Helper function to load the config text files ---
def _load_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8").strip()


# --- Helper function to load the resolver lists ---
def _load_resolver(name: str, path: pathlib.Path) -> str:
    raw = path.read_text(encoding="utf-8")
    return raw


# --- Export text constants ---
CONFIG_TEMPLATE = _load_text(BASE / "config_template.txt")
RESOLVER_HEADER = _load_text(BASE / "resolver_header.txt")

# ── Embedded app icon (base64 PNG, 256x256) ────────────────────
ICON_B64 = _load_text(BASE / "icon_b64.txt")


# --- Export resolver lists ---

#  WHITE DNS IRAN LIST  (from range-scout — pre-verified Iranian resolvers)
WHITE_DNS_UDP = _load_resolver("WHITE_DNS_UDP", RESOLVER_FILES["WHITE_DNS_UDP"])

#  IRAN IPv4 CIDR RANGES  (for supplemental IP sampling)
IRAN_CIDRS_RAW = _load_resolver("IRAN_CIDRS_RAW", RESOLVER_FILES["IRAN_CIDRS_RAW"])
BUILTIN_RESOLVERS = _load_resolver("BUILTIN_RESOLVERS", RESOLVER_FILES["BUILTIN_RESOLVERS"])