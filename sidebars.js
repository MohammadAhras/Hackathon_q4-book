// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      items: [
        'module-1/index',
        'module-1/chapter-1-ros2-fundamentals',
        'module-1/chapter-2-python-agents',
        'module-1/chapter-3-urdf-modeling',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      items: [
        'module-2/index',
        'module-2/chapter-1-gazebo-physics',
        'module-2/chapter-2-unity-environments',
        'module-2/chapter-3-sensor-simulation',
      ],
    },
  ],
};

module.exports = sidebars;