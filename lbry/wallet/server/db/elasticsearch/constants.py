INDEX_DEFAULT_SETTINGS = {
    "settings":
        {"analysis":
            {"analyzer": {
                "default": {"tokenizer": "whitespace", "filter": ["lowercase", "porter_stem"]}}},
            "index":
                {"refresh_interval": -1,
                 "number_of_shards": 1,
                 "number_of_replicas": 0,
                 "sort": {
                     "field": ["trending_mixed", "release_time"],
                     "order": ["desc", "desc"]
                 }}
        },
    "mappings": {
        "properties": {
            "claim_id": {
                "fields": {
                    "keyword": {
                        "ignore_above": 256,
                        "type": "keyword"
                    }
                },
                "type": "text",
                "index_prefixes": {
                    "min_chars": 1,
                    "max_chars": 10
                }
            },
            "height": {"type": "integer"},
            "claim_type": {"type": "byte"},
            "censor_type": {"type": "byte"},
            "trending_mixed": {"type": "float"},
            "release_time": {"type": "long"},
        }
    }
}

FIELDS = {
    '_id',
    'claim_id', 'claim_type', 'claim_name', 'normalized_name',
    'tx_id', 'tx_nout', 'tx_position',
    'short_url', 'canonical_url',
    'is_controlling', 'last_take_over_height',
    'public_key_bytes', 'public_key_id', 'claims_in_channel', 'channel_join_height',
    'channel_id', 'signature', 'signature_digest', 'is_signature_valid',
    'amount', 'effective_amount', 'support_amount',
    'fee_amount', 'fee_currency',
    'height', 'creation_height', 'activation_height', 'expiration_height',
    'stream_type', 'media_type', 'censor_type',
    'title', 'author', 'description',
    'timestamp', 'creation_timestamp',
    'duration', 'release_time',
    'tags', 'languages', 'has_source', 'reposted_claim_type',
    'reposted_claim_id', 'repost_count',
    'trending_group', 'trending_mixed', 'trending_local', 'trending_global',
}

TEXT_FIELDS = {'author', 'canonical_url', 'channel_id', 'claim_name', 'description', 'claim_id', 'censoring_channel_id',
               'media_type', 'normalized_name', 'public_key_bytes', 'public_key_id', 'short_url', 'signature',
               'signature_digest', 'stream_type', 'title', 'tx_id', 'fee_currency', 'reposted_claim_id', 'tags'}

RANGE_FIELDS = {
    'height', 'creation_height', 'activation_height', 'expiration_height',
    'timestamp', 'creation_timestamp', 'duration', 'release_time', 'fee_amount',
    'tx_position', 'channel_join', 'repost_count', 'limit_claims_per_channel',
    'amount', 'effective_amount', 'support_amount',
    'trending_group', 'trending_mixed', 'censor_type',
    'trending_local', 'trending_global',
}

ALL_FIELDS = RANGE_FIELDS | TEXT_FIELDS | FIELDS

REPLACEMENTS = {
    'name': 'normalized_name',
    'txid': 'tx_id',
    'reposted': 'repost_count'
}
