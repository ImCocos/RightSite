from .ability_schema import Query as ability_schema_query
from .category_schema import Query as category_schema_query
from .hero_schema import Query as hero_schema_query
from .item_schema import Query as item_schema_query
from .ability_type_schema import Query as ability_type_schema_query
from .cost_schema import Query as cost_schema_query
from .ability_cost_schema import Query as ability_cost_schema_query
from .per_schema import Query as per_schema_query
from .unit_schema import Query as unit_schema_query
from .item_class_schema import Query as item_class_schema_query
from .effect_schema import Query as effect_schema_query


all_schemas = [
    ability_schema_query,
    category_schema_query,
    hero_schema_query,
    item_schema_query,
    ability_type_schema_query,
    cost_schema_query,
    ability_cost_schema_query,
    per_schema_query,
    unit_schema_query,
    item_class_schema_query,
    effect_schema_query,
]
