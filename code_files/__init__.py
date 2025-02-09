from gym.envs.registration import register

register(
    id='Pygame-v0',
    entry_point='code_files.envs.env:CustomEnv',
    max_episode_steps=2000
)