from initialiser import *

creation_rate = 0.2
vaccinated_rate = 0.0
infected_rate=0.03
transmission_rate = 0.1

while transmission_rate <= 1.0 :
  # Helper processes
  agent_factory = AgentFactory(creation_rate=creation_rate,
                               vaccinated_rate=vaccinated_rate,
                               infected_rate=infected_rate,
                               transmission_rate=transmission_rate,
                               journeys=journeys,
                               entrance=entrance)
  renderer = Renderer(locations=locations,
                      agents=[],
                      delay=0.1)

  # Run simulation
  sim = Simulation(location=entrance, agents=[])
  sim.run(agent_factory=agent_factory,
          renderer=renderer,
          epoch=1000,
          verbose=False)
  agent_factory.print_info()
  sim.print_statistics()
  transmission_rate += 0.05
