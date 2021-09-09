from progress_bar import ProgressBar

# Progress bar visual tests/examples
if __name__ == '__main__':

    from time import sleep, time

    # Prefix, postfix, multiple levels and level removal test
    print('Simple progress bar and level removal test:')

    bar = ProgressBar()

    bar.set_progress_character('=')
    bar.set_current_progress_char('>')
    bar.set_empty_character('.')

    bar.set_prefix_expression('{time:2.2f} [')
    bar.set_postfix_expression('] {outer} - {inner}')

    bar.progress_char_length = 60
    bar.set_max(outer_level = 20, inner_level = 50)

    start_time = time()
    for i in range(20):

        bar.set_progress(i, level = 'outer_level')
        bar.set_postfix_arg('outer', i + 1)

        if i == 14:
            bar.remove_progress_level('inner_level')
            bar.set_postfix_expression('] {outer}')

        for j in range(100):

            bar.set_progress(j, level = 'inner_level', percent = True)
            bar.set_postfix_arg('inner', j + 1)
            bar.set_prefix_arg('time', time() - start_time)
            bar.print()

            sleep(0.01)

        bar.set_prefix_arg('time', time() - start_time)
        bar.print()
        sleep(0.07)
