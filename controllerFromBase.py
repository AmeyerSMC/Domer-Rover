import pygame

pygame.init()


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 25)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


def main():
    # Set the width and height of the screen (width, height), and name the window.
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Get ready to print.
    text_print = TextPrint()
    
    j = pygame.joystick.Joystick(0)

    # This dict can be left as-is, since pygame will generate a
    # pygame.JOYDEVICEADDED event for every joystick connected
    # at the start of the program.
    joysticks = {}

    done = False
    while not done:
        # Event processing step.
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN and j.get_button(1):
                print("Joystick button pressed.")
                if event.button == 0:
                    joystick = joysticks[event.instance_id]
                    if joystick.rumble(0, 0.7, 500):
                        print(f"Rumble effect played on joystick {event.instance_id}")

            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

            # Handle hotplugging
            if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        # Drawing step
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill((255, 255, 255))
        text_print.reset()

        # For each joystick:
        for joystick in joysticks.values():
            jid = joystick.get_instance_id()

            guid = joystick.get_guid()
            text_print.tprint(screen, f"GUID: {guid}")

            power_level = joystick.get_power_level()
            text_print.tprint(screen, f"Joystick's power level: {power_level}")
            
            text_print.tprint(screen, f"")
            
            a_lt = joystick.get_axis(4) + 1
            a_rt = joystick.get_axis(5) + 1
            b_lbumper = joystick.get_button(9)
            b_rbumper = joystick.get_button(10)
            
            text_print.tprint(screen, f"Left trigger value: {a_lt}")
            text_print.tprint(screen, f"Right trigger value: {a_rt}")
            text_print.tprint(screen, f"Left bumper value: {b_lbumper}")
            text_print.tprint(screen, f"Right pumper value: {b_rbumper}")
            
            a_leftx = joystick.get_axis(0)
            a_lefty =  joystick.get_axis(1) * -1
            a_rightx = joystick.get_axis(2)
            a_righty =  joystick.get_axis(3) * -1
            
            text_print.tprint(screen, f"")
            
            text_print.tprint(screen, f"Left joystick x: {a_leftx}")
            text_print.tprint(screen, f"Right joystick y: {a_lefty}")
            text_print.tprint(screen, f"Right joystick x: {a_rightx}")
            text_print.tprint(screen, f"Right joystick y: {a_righty}")
                        
            b_x = joystick.get_button(0)
            b_circle = joystick.get_button(1)
            b_square = joystick.get_button(2)
            b_triangle = joystick.get_button(3)
            
            text_print.tprint(screen, f"")
            
            text_print.tprint(screen, f"X button value: {b_x}")
            text_print.tprint(screen, f"Circle button value: {b_circle}")
            text_print.tprint(screen, f"Square button value: {b_square}")
            text_print.tprint(screen, f"Triangle button value: {b_triangle}")

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 30 frames per second.
        clock.tick(30)


if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()