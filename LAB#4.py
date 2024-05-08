import random

COMPONENT_PRICES = {
    'door': 2500,
    'outside_door': 8500,
    'window': 3450,
    'wall_module': 75000,
    'toilet_seat': 2995,
    'tab': 2350,
    'shower_cabin': 8300
}

HOUSE_COMPONENTS = {
    'floor': {
        'bed_room': {
            'windows': 2,
            'door': 1,
            'wall_module': 1
        },
        'bath_room': {
            'door': 1,
            'toilet_seat': 1,
            'tab': 1,
            'shower_cabin': 1,
            'wall_module': 1
        },
        'living_room': {
            'door': 1,
            'windows': 3,
            'wall_module': 1
        },
        'hall': {
            'outside_door': 1,
            'window': 1,
            'wall_module': 1
        },
        'garret': {
            'windows': 3,
            'door': 1,
            'wall_module': 1
        }
    }
}


class ConstructionMaterialAgent:
    def __init__(self, initial_materials, initial_money):
        self.materials = initial_materials
        self.money = initial_money

        for part in HOUSE_COMPONENTS['floor']:
            if part not in self.materials:
                self.materials[part] = {}
            for component, _ in HOUSE_COMPONENTS['floor'][part].items():
                if component not in self.materials[part]:
                    self.materials[part][component] = 0

    def sell_materials(self, components_needed, builder_id):
        total_cost = sum(
            COMPONENT_PRICES.get(component, 0) * quantity for part, components in components_needed.items() for
            component, quantity in components.items())

        if self.check_availability(components_needed) and self.money >= total_cost:
            print(f"Builder {builder_id} is buying:")
            for part, components in components_needed.items():
                for component, quantity in components.items():
                    self.materials[part][component] -= quantity
                    print(f"  - {quantity} units of {component} for {part}")

            self.money -= total_cost
            print(f"  Total cost: {total_cost}. Remaining money: {self.money}")
            return True
        return False

    def check_availability(self, components_needed):
        for part, components in components_needed.items():
            for component, quantity in components.items():
                if self.materials[part].get(component, 0) < quantity:
                    return False
        return True

    def receive_payment(self, amount):
        self.money += amount


class BuilderAgent:
    def __init__(self):
        self.num_houses_built = 0

    def build_house(self, construction_material_agent, builder_id):
        house_components = {part: components.copy() for part, components in HOUSE_COMPONENTS['floor'].items()}

        if construction_material_agent.sell_materials(house_components, builder_id):
            self.num_houses_built += 1
            return True
        else:
            return False


construction_material_agent = ConstructionMaterialAgent({
    'bed_room': {'windows': 0, 'door': 0, 'wall_module': 0},
    'bath_room': {'door': 0, 'toilet_seat': 0, 'tab': 0, 'shower_cabin': 0, 'wall_module': 0},
    'living_room': {'door': 0, 'windows': 0, 'wall_module': 0},
    'hall': {'outside_door': 0, 'window': 0, 'wall_module': 0},
    'garret': {'windows': 0, 'door': 0, 'wall_module': 0}
}, initial_money=10000000)

for part, components in HOUSE_COMPONENTS['floor'].items():
    for component, quantity in components.items():
        construction_material_agent.materials[part][component] += quantity * 10  # Sufficient for 10 houses

num_builder_agents = 5
builder_agents = [BuilderAgent() for _ in range(num_builder_agents)]

print(f"Initial money of Construction Material Agent: {construction_material_agent.money}")
for agent_id, builder_agent in enumerate(builder_agents, start=1):
    if builder_agent.build_house(construction_material_agent, agent_id):
        print(f"Builder {agent_id} successfully built a house.")
    else:
        print(f"Builder {agent_id} was unable to build a house due to insufficient materials or funds.")

for agent_id, builder_agent in enumerate(builder_agents, start=1):
    print(f"Builder {agent_id} built {builder_agent.num_houses_built} houses.")

print(f"Construction Material Agent has {construction_material_agent.money} money left.")
