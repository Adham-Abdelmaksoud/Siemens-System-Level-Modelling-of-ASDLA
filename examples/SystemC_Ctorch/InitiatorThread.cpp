#include "Initiator.h"
#include "extension.cpp"
using json = nlohmann::json;
using namespace std;
using namespace sc_core;
using namespace tlm;
using namespace torch;

void Initiator::sendDataThread()
{
    // Create a generic payload and using custom extension made in extension.cpp
    tlm::tlm_generic_payload trans;
    my_extension *test_extension_transaction = new my_extension;
    // changing the attribute `id` from 0 to 5
    test_extension_transaction->id = 5;
    // setting the extension
    trans.set_extension(test_extension_transaction);
    // setting the command
    trans.set_command(tlm::TLM_WRITE_COMMAND);
    sc_time delay;
    // send first time with `id` = 5
    init_socket->b_transport(trans, delay);
    test_extension_transaction->id = 12;
    // send second time with `id` = 12
    init_socket->b_transport(trans, delay);

    return;
}
