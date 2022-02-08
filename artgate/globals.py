from artgate.registries import ThreadSafeCategoryRegistry

global category_registry
category_registry = ThreadSafeCategoryRegistry()
